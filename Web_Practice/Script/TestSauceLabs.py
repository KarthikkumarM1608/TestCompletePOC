import Eventhandler
import CsvWriter
import LoginPage
import ProductsPage
import ShoppingCartPage
import CheckOutOne
import CheckOutTwo
import OrderConfirmationPage

def test_one_sauce():
  
  # Implementing Data Driven Test
  DDT.CSVDriver(Project.Variables.csv_file_path)

  # Login with the username and password
  login = LoginPage.Login()
  login.login(Project.Variables.Username, Project.Variables.Password)
  
  Log.Message("SauceLabs Order submission using DDT")
  
  row_counter = 0
  
  while not DDT.CurrentDriver.EOF():
    
    shopping_data = DDT.CurrentDriver.Value
    Log.AppendFolder(shopping_data["firstname"])
    
    # Search for the Products and adding to Cart
    products = ProductsPage.ProductsPage()
    products.find_product(shopping_data["itemname"])
    
    # clicking on Cart button in Products page
    products.click_cart_icon()
    
    # clicking on Checkout button in Shopping cart page 
    cart = ShoppingCartPage.ShoppingCart()
    cart.click_checkout_link()
    
    # Entering the Firstname, Lastname and Zip code in CheckoutOne page
    checkout_one = CheckOutOne.CheckOutOne()
    checkout_one.fill_your_info(shopping_data["firstname"], shopping_data["lastname"], shopping_data["zip"])
    
    checkout_one.click_continue()
    
    # Clicking Finish button in CheckoutTwo page
    checkout_two = CheckOutTwo.CheckOutTwo()
    payment_info = checkout_two.extract_payment_info()
    shipping_info = checkout_two.extract_shipping_info()
    
    checkout_two.click_finish()
    
    csv_file_path = Project.Variables.csv_file_path
    
    # Update the details in the CSV file
    CsvWriter.update_csv_data(csv_file_path, row_counter, payment_info, shipping_info)
    
    # Writing the details to Excel,
    #CsvWriter.write_csv(row_counter, payment_info, shipping_info)
    
    # Validating the checkpoint in OrderConfirmation page
    confirmation = OrderConfirmationPage.OrderConfirmationPage()
    confirmation.validate_checkpoint()
    
    confirmation.navigate_products_page()
    
    Log.PopLogFolder()
    
    DDT.CurrentDriver.Next()
    row_counter += 1
    
    
    
  
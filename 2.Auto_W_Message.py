import pywhatkit as pyw

try:
    phone_number = "+880555555555"
    # Ensure it's in the correct format
    message = "Hello! This is an instant message."
    
    pyw.sendwhatmsg_instantly(phone_number, message)
    print("✅ Message sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")





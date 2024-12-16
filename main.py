#basic discord webhook spammer
import time
import requests

webhook = input("Webhook: ")
message = input("Message: ")
wait_time = int(input("Waiting time (e.g. 2): "))
print("")

#spams message 
def main():
    #loop
    while True:
        try:
            hook = requests.post(webhook, json={'content': message})
            if hook.status_code == 204:
                print(f"Sent Message!")
        except:
            print("Something is wrong with the webhook provided!")
        time.sleep(wait_time)
    
if __name__ == "__main__":
    main()
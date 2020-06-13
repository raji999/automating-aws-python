try:
    def main():
        print(f"This script allows you to:\n-list all your instances.\n-Start an instance.\n-Stop an instance\n-Restart instance\n-Terminate instance/s.")
        print("_______________________________")
        user_promt = input(
            "Do you want to see all your instances now? Please enter yes, no or exit to finish: ")
        if user_promt.lower() == "yes" or user_promt.lower() == "y":
            list_instance()
            print(
                "___________________________________________________________________________")
            menu()
        elif user_promt.lower() == "no" or user_promt.lower() == "n":
            time.sleep(0.7)
            menu()

        elif user_promt.lower() == "exit":
            print("Goodbye......")
            sys.exit()
        else:
            print("Sorry, your entry was not valid.")
            try_again = input("Do you want to try again?: ")
            if try_again.lower() == "yes" or try_again.lower() == "y":
                main()
            else:
                print("GoodBye.....")
                sys.exit()

        return user_promt

    def list_instance():
        discribe_instances = ec2_cli.describe_instances()['Reservations']
        print("Getting your instances, one moment please.....")
        time.sleep(1.5)
        num = 0
        for items in discribe_instances:
            for values in items['Instances']:
                num += 1
                print(
                    f"{num}-Instance ID: {values['InstanceId']}, is currently {values['State']['Name']} in AZ: {values['Placement']['AvailabilityZone']}.")
        return None

    def menu():
        options = """Now we can execute one of the below actions:
            1. If you want to start an instance please enter 1.
            2. If you want to stop an instance please enter 2.
            3. If you want to reboot an instance please enter 3.
            4. If you want to terminate an instance please enter 4.
            5. Enter 5 to exit."""
        print("___________________________________________________________________________")
        print(options)
        select = input("Please enter one of the option: ")
        if select == "1" or select.lower() == "one" or select.lower() == "start":
            start_ec2s()
        elif select == "2" or select.lower() == "two" or select.lower() == "stop":
            stop_ec2s()
        elif select == "3" or select.lower() == "three" or select.lower() == "reboot":
            reboot_ec2s()
        elif select == "4" or select.lower() == "four" or select.lower() == "terminate":
            terminate_ec2()
        elif select == "5" or select.lower() == "five" or select.lower() == "exit" or select.lower() == "quit":
            print("GoodBye....."), sys.exit()
        else:
            print("Sorry, your entry was not valid.")
            try_again = input("Do you want to try again?: ")
            if try_again.lower() == "yes":
                menu()
            else:
                print("GoodBye.....")

    def start_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.start_instances(InstanceIds=[get_instance])
        print("Starting your ec2 instance, please wait.....")
        waiter = ec2_cli.get_waiter('instance_running')
        waiter.wait(InstanceIds=[get_instance])
        print("Good news, your instance is up and running.\nThank you!")
        return None

    def stop_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.stop_instances(InstanceIds=[get_instance])
        print("Stopping your ec2 instance, please wait.....")
        waiter = ec2_cli.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[get_instance])
        print("Your instance is now stopped.\nGoodbye!")
        return None

    def reboot_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.reboot_instances(InstanceIds=[get_instance])
        print("Restarting your ec2 instance, please wait.....")
        waiter = ec2_cli.get_waiter('instance_running')
        time.sleep(25)
        waiter.wait(InstanceIds=[get_instance])
        print("Your instance restarted sucessfully and is now up and running.\nThank you!")
        return None

    def terminate_ec2():
        final_notice = input(
            "Are your sure you want to terminate this instance?: ")
        if final_notice.lower() == "yes" or final_notice.lower() == 'y':
            get_instance = input("Please enter your instance id: ")
            ec2_cli.terminate_instances(InstanceIds=[get_instance])
            print("Terminating your ec2 instance, please wait.....")
            waiter = ec2_cli.get_waiter('instance_terminated')
            waiter.wait(InstanceIds=[get_instance])
            print(
                "Your instance is now terminated for good.\nThank you!")
        elif final_notice.lower() == "no" or final_notice.lower() == "n":
            print(
                "I'm glad you changed your mind. Mistakes are never good.\nGoodBye.....")
            sys.exit()
        else:
            print("Your entry was invalid. ")
            try_again = input("Would you like to try again?: ")
            if try_again.lower() == "yes" or try_again.lower() == "y":
                terminate_ec2()
            else:
                print("GoodBye.....")
        return None
    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)

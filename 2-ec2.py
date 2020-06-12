#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import boto3
from pprint import pprint
import sys
import time

lguilarte = boto3.session.Session(profile_name='lguilarte')
ec2_cli = lguilarte.client(service_name='ec2', region_name='us-east-1')


"""
# 1:
# List EC2 instances


def list_ec2s():
    response = ec2_cli.describe_instances()['Reservations']
    num = 0
    for items in response:
        for instances in items['Instances']:
            num += 1
            print(
                f"{num}-Instance ID is: {instances['InstanceId']}\nWith AMI id as : {instances['ImageId']}\nWas launched on: {instances['LaunchTime']}")
    return None


# 3:
# Working with volumes:


def vol():
    list_vlm = ec2_cli.describe_volumes()['Volumes']
    num = 0
    for items in list_vlm:
        num += 1
        print(
            f"{num}-{items['VolumeId']} is in AZ {items['AvailabilityZone']}")
    return None


# 4:
# Menu driven script to performe different status actions on EC2 instance.
"""


# 1- CONFIGURE WAITERS........
# 2- Implement an option that the user can chose if it want to start, stop, restart or teminate all instances in the account.


try:
    def main():
        options = """We can execute one of the below actions:
            1. If you want to start an instance please enter 1.
            2. If you want to stop an instance please enter 2.
            3. If you want to reboot an instance please enter 3.
            4. If you want to terminate an instance please enter 4.
            5. Enter 5 to exit."""
        print("__________________________")
        print(f"This script allows you to:\n1-list all your instances.\n2-Start instance/s.\n3-Stop instance/s.\n4-Restart instance/s\n5-Terminate instance/s.")
        user_promt = input(
            "Do you want to see all your instances before? Please enter yes, no or exit to finish: ")
        if user_promt.lower() == "yes" or user_promt == "1":
            list_instance()
            print(options)
            select = input("Please enter one of the option: ")
            if select == "1" or select.lower() == "one":
                start_ec2s()
            elif select == "2" or select.lower() == "two":
                stop_ec2s()
            elif select == "3" or select.lower() == "reboot":
                reboot_ec2s()
            elif select == "4" or select.lower() == "terminate":
                terminate_ec2()
        elif user_promt == "2" or user_promt.lower() == "no":
            time.sleep(0.7)
            print(options)
            select = input("Please chose one of the option: ")
            if select == "1" or select.lower() == "one":
                start_ec2s()
            elif select == "2" or select.lower() == "two":
                stop_ec2s()
            elif select == "3" or select.lower() == "reboot":
                reboot_ec2s()
            elif select == "4" or select.lower() == "terminate":
                terminate_ec2()
        elif user_promt.lower() == "exit":
            print("Goodbye......")
            sys.exit()
        else:
            print(
                "Sorry, You did not enter one of the five options. You can run the script again.\nGoodBye.....")
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

    def start_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.start_instances(InstanceIds=[get_instance])
        return None

    def stop_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.stop_instances(InstanceIds=[get_instance])
        return None

    def reboot_ec2s():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.reboot_instances(InstanceIds=[get_instance])

    def terminate_ec2():
        get_instance = input("Please enter your instance id: ")
        ec2_cli.terminate_instances(InstanceIds=[get_instance])
    if __name__ == "__main__":
        main()
except Exception as e:
    print(e)


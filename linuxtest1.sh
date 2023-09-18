#! /bin/bash

ip_address=$(hostname -i)
echo "LIST OF IP ADDRESS: ${ip_address}"


# Or Extracting lines that match the following pattern
ip=$(ip address| awk '/inet/ {print $2}' | grep -v ^::1 | grep -v ^127)

#displaying IP addresses
echo "LIST OF IP ADDRESSES"
echo "$ip"

# or for ec2
#internalipaddress=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4)

# Replace something in the file using sed command
sed 's/#Test/Linux/' test.txt

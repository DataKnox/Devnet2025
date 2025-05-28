# Cisco IOS-XE Terraform Configuration

This Terraform project configures a Cisco IOS-XE device using RESTCONF to create and manage network interfaces.

## Prerequisites

- Terraform >= 1.0
- Cisco IOS-XE device with RESTCONF enabled
- Network connectivity to the device

## Device Configuration

The device is configured with the following parameters:
- Host: 192.168.0.153
- Username: admin
- Password: password
- RESTCONF Port: 443 (HTTPS)

## Current Configuration

This project currently configures:
- Loopback interface 2 with IP address 1.1.1.1/32 using RESTCONF
- Uses the IETF interfaces YANG model for configuration

## Usage

1. Initialize Terraform:
```bash
terraform init
```

2. Review the planned changes:
```bash
terraform plan
```

3. Apply the configuration:
```bash
terraform apply
```

4. To destroy the configuration:
```bash
terraform destroy
```

## Security Note

The current configuration uses insecure connection (hostkey verification disabled) for demonstration purposes. In a production environment, you should:
- Use secure connection methods
- Store credentials in environment variables or a secure vault
- Enable hostkey verification
- Use proper SSL/TLS certificates 
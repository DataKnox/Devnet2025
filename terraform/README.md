# Linode Ubuntu Server Terraform Configuration

This Terraform configuration deploys an Ubuntu 24.04 server on Linode with the following specifications:
- Region: US Southeast (Atlanta)
- Instance Type: g6-standard-4 (4 shared CPU cores)
- Image: Ubuntu 24.04
- Features: SSH key authentication, automatic updates on first boot

## Prerequisites

1. [Terraform](https://www.terraform.io/downloads.html) installed (version >= 1.0)
2. A Linode account
3. A Linode API token
4. An SSH key pair

## Setup Instructions

1. Clone this repository
2. Copy the example variables file:
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```
3. Edit `terraform.tfvars` and fill in your values:
   - `linode_token`: Your Linode API token
   - `root_password`: A secure root password
   - `ssh_public_key`: Your SSH public key
   - Optionally modify other variables as needed

4. Initialize Terraform:
   ```bash
   terraform init
   ```

5. Review the planned changes:
   ```bash
   terraform plan
   ```

6. Apply the configuration:
   ```bash
   terraform apply
   ```

7. After successful deployment, the output will show the instance's IP address.

## Accessing the Server

Once deployed, you can access the server using SSH:
```bash
ssh root@<instance_ip>
```

## Cleanup

To destroy the infrastructure when no longer needed:
```bash
terraform destroy
```

## Security Notes

- Never commit `terraform.tfvars` to version control
- Keep your Linode API token secure
- Use a strong root password
- Consider using SSH key authentication exclusively 
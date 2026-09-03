# providers is specific for terraform to connect to a specific cloud
# e.g. Azure, AWS, GCP

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.4"
    }
  }
  required_version = ">= 1.13"
}

provider "azurerm" {
  features {}
}
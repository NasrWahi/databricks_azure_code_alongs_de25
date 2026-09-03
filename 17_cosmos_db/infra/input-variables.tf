variable "resource_group_name" {
  default = "rg-cosmos-test-tf"
  type    = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "swedencentral"
}
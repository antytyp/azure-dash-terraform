variable "resource_group_name" {
  type    = string
  default = "rg-dash"
}

variable "location" {
  type        = string
  default     = "westeurope"
  description = "Location of the resource group."
}

variable "web_app_name" {
  type        = string
  default     = "pdyrlagadashwebapp"
  description = "Globally unique app name"
}

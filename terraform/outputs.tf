output "dash_url" {
  value = "https://${azurerm_linux_web_app.dash.default_hostname}"
}

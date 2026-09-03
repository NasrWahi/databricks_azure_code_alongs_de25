resource "azurerm_cosmosdb_account" "acc" {
  name                = "cosmos-acc-${random_string.suffix.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  # no geo redundancy
  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }
  # same client session, always read own writes, reads don't go backward
  consistency_policy {
    consistency_level = "Session"
  }

  capabilities {
    name = "EnableServerless"
  }
}


# sql-like syntax
resource "azurerm_cosmosdb_sql_database" "db" {
  name                = "FilmReviewDB"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.acc.name
}

resource "azurerm_cosmosdb_sql_container" "films_container" {
  name                  = "Films"
  resource_group_name   = azurerm_resource_group.rg.name
  account_name          = azurerm_cosmosdb_account.acc.name
  database_name         = azurerm_cosmosdb_sql_database.db.name
  partition_key_paths   = ["/year"]
  partition_key_version = 2
}
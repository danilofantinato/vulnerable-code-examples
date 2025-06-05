# Remediated code:

# For AWS:
resource "aws_instance" "example" {
  associate_public_ip_address = false
}
resource "aws_dms_replication_instance" "example" {
  publicly_accessible = false
}

# For Azure:
resource "azurerm_postgresql_server" "example" {
  public_network_access_enabled = false
}
resource "azurerm_postgresql_server" "example" {
  public_network_access_enabled = false
}
resource "azurerm_kubernetes_cluster" "production" {
  api_server_authorized_ip_ranges = [] # Restrict access to authorized IP ranges
  default_node_pool {
    enable_node_public_ip = false
  }
}

# For GCP:
resource "google_compute_instance" "example" {
  network_interface {
    network = "default"

    access_config {
      # No public IP assigned
    }
  }
}
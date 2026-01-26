variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "location" {
  description = "Project Location"
  default     = "ASIA"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "demo-bucket-dtalks-decamp-2026"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "project" {
  description = "Project Location"
  default     = "project-4d53d712-269c-4bf0-bd2"
}

variable "region" {
  description = "Region"
  default     = "asia-southeast1"
}

resource "google_storage_bucket" "staic-ste" {
  name          = "bkt-ranking-dataengginering"
  location      = "US"
  force_destroy = true
}

# resource "google_storage_bucket_object" "static_site"{
# name="batsmen_ranking.csv"
# source = "../batsmen_ranking.csv"
# bucket = google_storage_bucket.website.name
# }
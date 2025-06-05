# AWS
resource "aws_iam_policy" "example" {
  name = "least_privilege_policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Effect   = "Allow"
        Resource = [
          aws_s3_bucket.mybucket.arn,
          "${aws_s3_bucket.mybucket.arn}/*"
        ]
      }
    ]
  })
}

# GCP
resource "google_project_iam_binding" "example" {
  project = "example"
  role    = "roles/viewer"

  members = [
    "user:jane@example.com",
  ]
}
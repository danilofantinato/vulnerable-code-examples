resource "aws_api_gateway_method" "compliantapi" {
  authorization = "AWS_IAM"
  http_method   = "GET"

  request_models = {
    "application/json" = aws_api_gateway_model.request_model.name
  }

  request_validator_id = aws_api_gateway_request_validator.request_validator.id
}

resource "aws_api_gateway_model" "request_model" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  name        = "RequestModel"
  description = "Request model for the API"
  content_type = "application/json"

  schema = <<EOF
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "RequestModel",
  "type": "object",
  "properties": {
    "userId": {
      "type": "string"
    },
    "requestData": {
      "type": "object"
    }
  },
  "required": [
    "userId",
    "requestData"
  ]
}
EOF
}

resource "aws_api_gateway_request_validator" "request_validator" {
  rest_api_id                 = aws_api_gateway_rest_api.api.id
  name                        = "RequestValidator"
  validate_request_body       = true
  validate_request_parameters = true
}
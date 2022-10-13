provider "aws" {
  region  = "us-west-2"
  profile = "tackle-mfa"
  assume_role {
    role_arn = "arn:aws:iam::003526222725:role/dept/eng/dev-access-role"
  }
}

provider "launchdarkly" {
  access_token = module.tkl_ld_tf.sdk_token
}

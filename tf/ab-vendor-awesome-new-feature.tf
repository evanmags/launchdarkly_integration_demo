resource "launchdarkly_feature_flag" "awesome_feature" {
  project_key = module.tkl_ld_tf.project_tackle
  key         = "ab-vendor-awesome-new-feature"
  name        = "Awesome Test Feature For LaunchDarkly Demo!!!"

  variation_type = "string"
  variations {
    value = "default"
    name  = "Default Value"
  }

  variations {
    value = "version1"
    name  = "ASCII Cats"
  }

  variations {
    value = "version2"
    name  = "Rick Roll"
  }

  defaults {
    on_variation  = 0
    off_variation = 0
  }

  client_side_availability {
    using_environment_id = true
  }

  tags = [
    "demo",
    "podinternalplatform",
    "terraform-managed"
  ]
}

resource "launchdarkly_feature_flag_environment" "awesome_feature_dev_env" {
  flag_id = launchdarkly_feature_flag.awesome_feature.id
  env_key = module.tkl_ld_tf.environment_dev

  on = true

  rules {
    variation = 2
    clauses {
      attribute = "type"
      op        = "in"
      values    = ["staff"]
      negate    = false
    }
  }

  fallthrough {
    variation = 0
  }
  off_variation = 0
}

# resource "launchdarkly_feature_flag_environment" "awesome_feature_other_envs" {
#   for_each = toset([
#     module.tkl_ld_tf.environment_test,
#     module.tkl_ld_tf.environment_staging,
#     module.tkl_ld_tf.environment_production,

#   ])

#   flag_id = launchdarkly_feature_flag.awesome_feature.id
#   env_key = each.key

#   rules {
#     variation = 1
#     clauses {
#       attribute = "vendorid"
#       op        = "in"
#       values    = []
#       negate    = false
#     }
#   }

#   fallthrough {
#     variation = 0
#   }
#   off_variation = 0
# }

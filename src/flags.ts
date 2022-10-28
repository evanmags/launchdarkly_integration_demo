export const FEATURE_FLAG_AWESOME_FEATURE = "ab-vendor-awesome-new-feature"
export type FlagMap = {
    [FEATURE_FLAG_AWESOME_FEATURE]: 'default' | 'version1' | 'version2'
}

export const localFlags = {
    [FEATURE_FLAG_AWESOME_FEATURE]: 'default'
}

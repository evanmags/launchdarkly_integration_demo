/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_AWESOME_SERVICE_URL: string
  readonly VITE_AUTH_SERVICE_URL: string
  readonly VITE_LD_CLIENT_SIDE_ID: string
  readonly VITE_AUTH_TOKEN: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

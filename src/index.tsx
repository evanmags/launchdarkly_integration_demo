import React, { useEffect, useState } from 'react'
import ReactDOM from 'react-dom'

import ReactPlayer from 'react-player/lazy'

import { FeatureFlagServiceProvider, useFeatureFlagService, TackleAuthServiceProvider } from '@tackle-io/tackle-auth-tools'
import { useAwesomeService } from './AwesomeService'

const FEATURE_FLAG_AWESOME_FEATURE = "ab-vendor-awesome-new-feature"
type FlagMap = {
    [FEATURE_FLAG_AWESOME_FEATURE]: 'default' | 'version1' | 'version2'
}

const FlaggedDisplayComponent = () => {
    const asvc = useAwesomeService(import.meta.env.VITE_AWESOME_SERVICE_URL)

    const ffs = useFeatureFlagService<FlagMap>()

    const flagValue = ffs.getFlag(FEATURE_FLAG_AWESOME_FEATURE, "default")

    const [displayData, setDisplayData] = useState<string>();
    useEffect(() => { asvc.getData().then(setDisplayData) }, [flagValue])

    switch (flagValue) {
        case 'version1':
            return <pre>{displayData}</pre>
        case 'version2':
            return <ReactPlayer
                playing={displayData ? true : false}
                muted={true}
                controls={true}
                url={displayData as string} />
        default:
            return <h3>{displayData}</h3>
    }
}

const LoadingMessage = () => <p>🧙‍♂️🪄✨ bipity bopity tag me on motivosity 🧙‍♂️🪄✨</p>

const App = () =>
    <>
        <p>Welcome To My Demo!</p>
        <TackleAuthServiceProvider authServiceUrl={import.meta.env.VITE_AUTH_SERVICE_URL}>
            <FeatureFlagServiceProvider
                authToken={import.meta.env.VITE_AUTH_TOKEN}
                clientSideID={import.meta.env.VITE_LD_CLIENT_SIDE_ID}
                App={FlaggedDisplayComponent}
                Loader={LoadingMessage}
            />
        </TackleAuthServiceProvider>
    </>


ReactDOM.render(<App />, document.querySelector('root'))

export class AwesomeService {
    serviceUrl: string

    constructor(serviceUrl: string) {
        this.serviceUrl = serviceUrl

    }

    getData = async (): Promise<string> => {
        return fetch(`${this.serviceUrl}/data`, {headers: { Authorization: import.meta.env.VITE_AUTH_TOKEN}}).then(res => res.text())
    }
}

export const useAwesomeService = (serviceUrl: string): AwesomeService => new AwesomeService(serviceUrl)

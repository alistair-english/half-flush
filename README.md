# half-flush
Checks to see if your public IP has changed

## Setup Instructions
1. Create a google account to send emails from and generate an "app password": https://support.google.com/accounts/answer/185833?hl=en
    - note, you have to first turn on two step verification: https://support.google.com/accounts/answer/185839?sjid=8122969288981557883-AP
    - then, you can go to: https://myaccount.google.com/apppasswords
2. Create a .env file with the following entries:

    `half-flush/.env`
    ```
    EMAIL_SENDER=<your gmail email>
    EMAIL_PASSWORD=<your "app password">
    EMAIL_RECIPENTS=<emails;separated;by;semicolon>
    ```
3. Install Docker Engine using the apt repository
    - https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
        - install the latest version
        - note, this is Docker **Engine** NOT Docker Desktop (which is what we want)
    - add your user to the docker group
        ```bash
        sudo groupadd docker
        ```
        ```bash
        sudo usermod -aG docker $USER
        ```
        - log out and back in for this to take effect
4. build and run the container using docker compose:
    ```bash
    docker compose up -d
    ```
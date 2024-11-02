# Review classification

Reviews are classified as Computer Generated or Human written. Uses RoBERTa model under the hood.

## Build the docker file 

1. Clone the Repository:

    ```bash
    git clone https://github.com/SreeHarshan/Review-classification-backend
    cd Review-classification-backend
    ```
2. Install docker, if it is not installed
* Ubuntu
    ```bash
    sudo apt install docker
    ```
* Arch
    ```bash
    sudo pacman -S docker
    ```
   
3. Install the requirements
    ```bash
    pip install -r requirements
    ```

4. Build the docker image 
    ```bash
    docker build -t <username>/<docker-image-name>:<version> .
    ```
5. Save the docker image to a file [OPTIONAL]
   ```bash
   docker image save <image-name> -o <tar-file-name>
   ```

6. Run the docker image
   ```bash
   docker run --network host -p 8000:8000 -v /tmp:/tmp -v /home:/home <docker-image-name>
   ```
    
**Note**
- The server runs on port 8000 and ip of 0.0.0.0, if you want to change the port or ip of server you can pass the port, ip as an env variable to docker by adding `docker run -e PORT=xxxx HOST=xxx.xxx.x.x ...`.
- The first prediction will take time as it has to load the RoBERTa model.
- The docker image can be saved into a file to load into another computer.

Future works
- Add weights file to make the model load faster

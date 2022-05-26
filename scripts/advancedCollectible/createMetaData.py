import os
from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import get_breed
from metadata.sampleMetaData import metaData_template
from pathlib import Path
import requests
import json

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def main():
    print(AdvancedCollectible)
    advancedCollectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advancedCollectible.tokenCounter()
    print(f"You have {number_of_advanced_collectibles} collectibles")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advancedCollectible.tokenIdToBreed(token_id))
        metaData_file = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"

        collectible_metaData = metaData_template

        if Path(metaData_file).exists():
            print(f"{metaData_file} already exits! Delete it to overwrite")
        else:
            print(f"Creating Meta Data file: {metaData_file}")

            # Create folder or not!

            if not Path(f"./metadata/{network.show_active()}/").exists():
                os.makedirs(f"./metadata/{network.show_active()}/")
                print("Folder created")
            collectible_metaData["name"] = breed
            collectible_metaData["description"] = f"An adorable {breed} pup!"
            image_file_name = f"./img/{breed.lower()}.png"

            image_uri = None

            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_file_name)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]

            collectible_metaData["image_uri"] = image_uri
            # print(metaData_file)
            print("Start")
            with open(metaData_file, "w") as outfile:
                json.dump(collectible_metaData, outfile)
            if os.getenv("UPLOAD_IPFS") == "true":

                upload_to_ipfs(metaData_file)

        print(metaData_file)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfsURL = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        print(ipfsURL + endpoint)
        response = requests.post(ipfsURL + endpoint, files={"file": image_binary})
        print(response)
        ipfs_hash = response.json()["Hash"]
        # ./img/PUG.png => PUG.png
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri

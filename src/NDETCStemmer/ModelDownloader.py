import gdown
import os
import requests

import huggingface_hub as hf_hub

from tqdm import tqdm
from checksumdir import dirhash
from abc import ABC, abstractmethod

class ModelPath:
    def __init__(
        self,
        w2vec_wiki_id_case: 'str',
        w2vec_wiki_id_case_trainables_syn1neg_npy: 'str',
        w2vec_wiki_id_case_wv_vectors_npy: 'str',
    ) -> None:
        self.w2vec_wiki_id_case = w2vec_wiki_id_case
        self.w2vec_wiki_id_case_trainables_syn1neg_npy = (
            w2vec_wiki_id_case_trainables_syn1neg_npy
        )
        self.w2vec_wiki_id_case_wv_vectors_npy = w2vec_wiki_id_case_wv_vectors_npy


class ModelDownloaderAbstract(ABC):
    @abstractmethod
    def download_model(self) -> "ModelPath":
        pass


class HuggingfaceModelDownloader(ModelDownloaderAbstract):
    def __init__(self) -> None:
        self.repo_id = "kaenova/NDETCStemmer"

    def download_model(self) -> "ModelPath":
        w2vec_wiki_id_case_path = hf_hub.hf_hub_download(
            repo_id=self.repo_id,
            filename="w2vec_wiki_id_case",
        )
        w2vec_wiki_id_case_trainables_syn1neg_npy_path = hf_hub.hf_hub_download(
            repo_id=self.repo_id,
            filename="w2vec_wiki_id_case.trainables.syn1neg.npy",
        )
        w2vec_wiki_id_case_wv_vectors_npy_path = hf_hub.hf_hub_download(
            repo_id=self.repo_id,
            filename="w2vec_wiki_id_case.wv.vectors.npy",
        )
        return ModelPath(w2vec_wiki_id_case_path, 
                         w2vec_wiki_id_case_trainables_syn1neg_npy_path, 
                         w2vec_wiki_id_case_wv_vectors_npy_path)


class GoogleDriveModelDownloader(ModelDownloaderAbstract):
    def __init__(self):
        self._model_1_id = "1DJ_u_xKSXmgS_CsM0xlB5rIznnDVfz-w"
        self._model_2_id = "1DQhPp-D3o0e-x3PfJd2Il3vf7wVgZu4J"
        self._model_3_id = "1zCn5YINEC82cZ1SH-nB4WXUvuELCzKu-"
        self._md5 = "f94b050f583fd7fedbf53c88d2ec8698"

        self._path = os.path.dirname(__file__)
        self._path = os.path.join(self._path, "Model")

    def download_model(self):
        if not os.path.exists(self._path):
            print("Model missing, downloading new model....")
            os.mkdir(self._path)
            print("\nDownloading Model 1/3")
            gdown.download(
                id=self._model_1_id,
                output=os.path.join(self._path, "w2vec_wiki_id_case"),
            )

            print("\nDownloading Model 2/3")
            gdown.download(
                id=self._model_2_id,
                output=os.path.join(
                    self._path, "w2vec_wiki_id_case.trainables.syn1neg.npy"
                ),
            )

            print("\nDownloading Model 3/3")
            gdown.download(
                id=self._model_3_id,
                output=os.path.join(self._path, "w2vec_wiki_id_case.wv.vectors.npy"),
            )
        
        return ModelPath(
			os.path.join(self._path, "w2vec_wiki_id_case"), 
			os.path.join(self._path, "w2vec_wiki_id_case.trainables.syn1neg.npy"), 
			os.path.join(self._path, "w2vec_wiki_id_case.wv.vectors.npy")
		)


class CustomLinkModelDownloader(ModelDownloaderAbstract):
    """
    # CustomModelDownloader

    This class is used to create a downloader instance using custom external links.
    It will download all data needed and check the hash if its a matching with the original models.

    ### Params
    model_1: str: Link to download with original file name `w2vec_wiki_id_case`

    model_2: str: Link to download with original file name `w2vec_wiki_id_case.trainables.syn1neg.npy`

    model_3: str: Link to download with original file name `w2vec_wiki_id_case.wv.vectors.npy`
    
## Usage
	
```python
from NDETCStemmer import NDETCStemmer, CustomLinkModelDownloader

downloader = CustomLinkModelDownloader(
	model_1="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case",
	model_2="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case.trainables.syn1neg.npy",
	model_3="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case.wv.vectors.npy"
)
stemmer=NDETCStemmer(downloader=downloader)
# stemming process
output=stemmer.stem('boleh saya memerah lembu ini')
print(output)
#boleh saya perah lembu ini
```
    """

    def __init__(self, model_1: str, model_2: str, model_3: str):
        self._md5 = "f94b050f583fd7fedbf53c88d2ec8698"

        self.model_1 = model_1
        self.model_2 = model_2
        self.model_3 = model_3

        self._path = os.path.dirname(__file__)
        self._path = os.path.join(self._path, "Model")

    def _downloadFile(self, url: str, fname: str):
        CHUNK_SIZE = 1024
        resp = requests.get(url, stream=True)
        total = int(resp.headers.get("content-length", 0))
        with open(fname, "wb") as file, tqdm(
            desc=fname,
            total=total,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=CHUNK_SIZE):
                size = file.write(data)
                bar.update(size)

    def download_model(self):
        if not os.path.exists(self._path):
            print("Model missing, downloading new model....")
            os.mkdir(self._path)
            print("\nDownloading Model 1/3")
            fname = os.path.join(self._path, "w2vec_wiki_id_case")
            self._downloadFile(self.model_1, fname)

            print("\nDownloading Model 2/3")
            fname = os.path.join(
                self._path, "w2vec_wiki_id_case.trainables.syn1neg.npy"
            )
            self._downloadFile(self.model_2, fname)

            print("\nDownloading Model 3/3")
            fname = os.path.join(self._path, "w2vec_wiki_id_case.wv.vectors.npy")
            self._downloadFile(self.model_3, fname)
        
        return ModelPath(
			os.path.join(self._path, "w2vec_wiki_id_case"), 
			os.path.join(self._path, "w2vec_wiki_id_case.trainables.syn1neg.npy"), 
			os.path.join(self._path, "w2vec_wiki_id_case.wv.vectors.npy")
		)

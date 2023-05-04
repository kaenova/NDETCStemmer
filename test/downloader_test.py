import unittest
from NDETCStemmer import (
    NDETCStemmer,
    GoogleDriveModelDownloader,
    CustomLinkModelDownloader
)

class Downloader(unittest.TestCase):

    def test_default_downloader(self):
        #init stemmer
        stemmer=NDETCStemmer()
        # stemming process
        output=stemmer.stem('boleh saya memerah lembu ini')
        self.assertEqual("boleh saya perah lembu ini ", output)
        output = stemmer.stem('bibirnya memerah tangannya jadi selengket madu')
        self.assertEqual("bibir merah tangan jadi lengket madu ", output)
        

    def test_google_drive_downloader(self):
        #init stemmer
        stemmer=NDETCStemmer(
            downloader=GoogleDriveModelDownloader()
        )
        # stemming process
        output=stemmer.stem('boleh saya memerah lembu ini')
        self.assertEqual("boleh saya perah lembu ini ", output)
        output = stemmer.stem('bibirnya memerah tangannya jadi selengket madu')
        self.assertEqual("bibir merah tangan jadi lengket madu ", output)
        
    def test_custom_link_downloader(self):
        # Init Custom Link Model Downloader
        downloader = CustomLinkModelDownloader(
            model_1="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case",
            model_2="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case.trainables.syn1neg.npy",
            model_3="https://is3.cloudhost.id/s3.kaenova.my.id/NDETCStemmer/Model/w2vec_wiki_id_case.wv.vectors.npy"
        )
        
        #init stemmer
        stemmer=NDETCStemmer(
            downloader=downloader
        )
        
        # stemming process
        output=stemmer.stem('boleh saya memerah lembu ini')
        self.assertEqual("boleh saya perah lembu ini ", output)
        output = stemmer.stem('bibirnya memerah tangannya jadi selengket madu')
        self.assertEqual("bibir merah tangan jadi lengket madu ", output)

if __name__ == '__main__':
    unittest.main()
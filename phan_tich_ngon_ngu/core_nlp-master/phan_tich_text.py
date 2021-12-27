from tokenization.crf_tokenizer import CrfTokenizer

# crf_tokenizer_obj = CrfTokenizer()
# crf_tokenizer_obj.train('D:/Project/voice_recognization/phan_tich_ngon_ngu/core_nlp-master/data/tokenized/samples/training')
# Note: If you trained your model, please set correct model path and do not train again!
crf_tokenizer_obj = CrfTokenizer(model_path='D:/Project/voice_recognization/phan_tich_ngon_ngu/core_nlp-master/models/vi-segmentation.crfsuite')

test_sent = "Thuế thu nhập cá nhân bật nhạc mở nhạc bật đèn mở đèn"
tokenized_sent = crf_tokenizer_obj.get_tokenized(test_sent)
print(tokenized_sent)

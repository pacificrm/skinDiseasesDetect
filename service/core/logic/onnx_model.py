import onnxruntime as rt
import cv2
import numpy as np
import service.main as s
import time
def skindisease_detector(img_array):
    # if len(img_array.shape)==2:
    #     img_array=
    
    time_init=time.time()
    test_image=cv2.resize(img_array,(256,256))
    im=np.float32(test_image)
    img_array=np.expand_dims(im,axis=0)

    onn_pred=s.m_q.run(['dense'], {"input_1":img_array})

    time_elapsed=time.time()-time_init
    diseaselist= ['Acne', 'Actinic_Keratosis', 'Benign_tumors', 'Bullous', 'Candidiasis', 'DrugEruption', 'Eczema', 'Infestations_Bites', 'Lichen', 'Lupus', 'Moles', 'Psoriasis', 'Rosacea', 'Seborrh_Keratoses', 'SkinCancer', 'Sun_Sunlight_Damage', 'Tinea', 'Unknown_Normal', 'Vascular_Tumors', 'Vasculitis', 'Vitiligo', 'Warts']
    disease=diseaselist[np.argmax(onn_pred[0][0])]
    return {"disease":disease,"time": str(time_elapsed)}
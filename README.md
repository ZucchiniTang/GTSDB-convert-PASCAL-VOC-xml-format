# Converting GTSDB 'gt.txt' into '*.xml' PASCAL VOC format
## Step:
1. Download GTSDB dataset
2. Change *gt.txt* to *gt_test.txt*+*gt_train.txt*.
3. Run code *gtsdb_convert_xml.py*, this step will create two folders **test_anno_xml** and **train_anno_xml**, which include created *\*.xml* inside. (If you don't want to create folder by yourself, you can use two folders **test_anno_xml** and **train_anno_xml** as groundtruth directly)

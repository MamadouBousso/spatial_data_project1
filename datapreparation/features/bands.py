class Bands{
  
  def __init__(self,path,bands):
    self.path = path
    self.bands = bands
  
  def get_band(self):
    band_path = []
    for band in self.bands:#Loops over bands list
        for file in os.listdir(self.path): #loops over all the files in the data directory
            ext = file[-7:]# slice the filename to get the last 7 characters. So  the band filenames result in BO1.jp2, B02.jp2 and so on
            if band in ext: #check if the current filename has the band digits from list  
                band_path.append(os.path.join(data_path,file)) #if match, append the whole extension to a list
    return band_path #return the list

  #translate image into tif
  def translate_img_to_tif(self,bands_path):
    for file in bands_path:
        image = gdal.Open(file)
        name = file[-7:-4]
        gdal.Translate(f'../data/outputs/{name}.tif',image)


  
}
#requirements: google_images_download module
#pip install google_images_download to download the module
#using this module as this is the simplest tool to download images from google while providing really flexible options
#which cam be passed as arguments

#importing google_images_download module 

from google_images_download import google_images_download  

#create instance/object

response = google_images_download.googleimagesdownload()  

keyword = input("Enter keyword to search image for: ")  #keyword for which we will be downloading the images
  
def downloadimages(query): #function to download images for the passed query keyword

    # keywords is the search query 

    # format is the image file format 

    # limit is the number of images to be downloaded 

    # print urs is to print the image file url 

    # size is the image size which can 

    # be specified manually ("large, medium, icon, etc)

    arguments = {"keywords": query, 

                 "format": "jpg", 

                 "limit":2,

                 "print_urls":True, 

                 "size": "medium"}

    try: 

        response.download(arguments) 

      

    # Handling File NotFound Error     
    #remove the parameters/arguments to expand search 

    except FileNotFoundError:  

        arguments = {"keywords": query}







           

          

# Providing arguments for the searched query 

        try: 

            # Downloading the photos based 

            # on the given arguments 

            response.download(arguments)  

        except: 

            pass

  
# Driver Code 
downloadimages(keyword)  
print()

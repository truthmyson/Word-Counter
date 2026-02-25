from file_manager import Filemanager
import io # for memory byte streaming
import time

def count_words(encoded_file, file_type: str) -> object:
    """
    open the file, read and return the total number of words
    
    :param encoded_file: encoded file base64
    :param file_type: the type of the file (txt,csv,docx,pdf)
    :file_type: str
    :return: return an object
    :rtype: object
    """
    # gather file info
    response = {'data': {}}

    try:
        with io.BytesIO(encoded_file) as file_stream:
            # initialise file manager
            manager = Filemanager(file_stream)

            # work on text and csv files
            if file_type.lower() in ['.txt', '.csv']:
                response = manager.TextManager()

            # work on document files
            elif file_type.lower() in ['.docx']:
                response = manager.DocxManager()
                
            # work on pdf files
            elif file_type.lower() in ['.pdf']:
                response = manager.PDFManager()
                
            else:
                now = time.localtime()
                response['data']['error_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
                response['status'] = 'error'
                response['data']['message'] = f'unsupported file type `{file_type}` . please upload pdf, doxc, csv, or txt.'
    except Exception as e:
        now = time.localtime()
        response['data']['error_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
        response['status'] = 'error'
        response['data']['message'] = f"file stream processing error: {e}"
    
    # return the final response
    return response

        
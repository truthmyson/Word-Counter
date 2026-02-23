import docx
import fitz #pymupdf
import time


class Filemanager:
    # A class to manage files and return the total words in them
    def __init__(self, base64_content):
        """
        initialise the content of the file

        :param base64_content: the content of the file in base64 encoding
        """
        self.base64_content = base64_content
        self.response = {'data': {}}


    def TextManager(self) -> object:
        """
        work on text and csv files

        :return: return an object
        :rtype: object
        """
        try:
            # work on text and csv files 
            self.base64_content.seek(0)
            text = self.base64_content.read().decode('utf-8', errors='replace')
            # perform data cleaning and processing
            text = text.replace('\n', ' ').replace('-', ' ').replace('_', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ').replace('\n\n', ' ').replace('\n\n\n', ' ').strip().lower()

            words = text.split()

            self.response['data']['word_count'] = len(words)
            # Current local time
            now = time.localtime()
            self.response['data']['processed_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            self.response['status'] = 'success'
            self.response['data']['file_type'] = 'txt'
            return self.response
        except Exception as e:
            self.response['status'] = 'error'
            self.response['data']['message'] = f"Plaintext processing error: {e}"
            now = time.localtime()
            self.response['data']['error_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            return self.response

    
    def DocxManager(self) -> object:
        """
        work on document files

        :return: return an object
        :rtype: object
        """
        try:
            self.base64_content.seek(0)
            document = docx.Document(self.base64_content)
            text = ''
            for para in document.paragraphs:
                text += para.text + ' '
            # perform data cleaning and processing
            text = text.replace('\n', ' ').replace('-', ' ').replace('_', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ').replace('\n\n', ' ').replace('\n\n\n', ' ').strip().lower()
            
            words = text.split()
            
            self.response['data']['word_count'] = len( words)
            # Current local time
            now = time.localtime()
            self.response['data']['processed_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            self.response['status'] = 'success'
            self.response['data']['file_type'] = 'docx'
            return self.response
        except Exception as e:
            self.response['status'] = 'error'
            self.response['data']['message'] = f"Document processing error: {e}"
            now = time.localtime()
            self.response['data']['error_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            return self.response

    
    def PDFManager(self) -> object:
        """
        work on pdf files

        :return: return an object
        :rtype: object
        """
        try:
            self.base64_content.seek(0)
            with fitz.open(stream=self.base64_content, filetype='pdf') as pdf:
                text = ''
                for page in pdf:
                    text += page.get_text() + ' '
                # perform data cleaning and processing
                text = text.replace('\n', ' ').replace('-', ' ').replace('_', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ').replace('\n\n', ' ').replace('\n\n\n', ' ').strip().lower()
                
                words = text.split()
            
                self.response['data']['word_count'] = len( words)
            # Current local time
            now = time.localtime()
            self.response['data']['processed_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            self.response['status'] = 'success'
            self.response['data']['file_type'] = 'pdf'
            return self.response
        except Exception as e:
            self.response['status'] = 'error'
            self.response['data']['message'] = f"PDF processing error: {e}"
            now = time.localtime()
            self.response['data']['error_time'] = time.strftime("%Y-%m-%d %H:%M:%S", now) # format time
            return self.response
        
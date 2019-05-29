import os
import tempfile
from PIL import Image
import shutil

from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

#from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse #we can user either one of these for reverse

from rest_framework import status

from status.models import Status
from django.conf import settings

# Create your tests here.

User=get_user_model()

class StatusAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testcfeuser', email='cfe@gmail.com')
        user.set_password("yehcfe")
        user.save()

        status_obj = Status.object.create(user=user, content='Hello there')

    def test_statuses(self):
        self.assertEqual(Status.object.count(), 1)

    def status_user_token(self):
        #for login user test
        auth_url = api_reverse('api-auth:login')
        auth_data = {'username':'testcfeuser',
                'password':'yehcfe',
                }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token=response.data.get("token", 0)
        self.client.credentials(HTTP_AUTHORIZATION = 'JWT ' + token)


    def create_item(self):
        self.status_user_token()

        #for status object create test
        url = api_reverse('api-status:list')
        data={'content':'some cool test content'}
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)
        return response.data

    def test_status_create(self):
        data=self.create_item()
        data_id=data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id':data_id})
        rud_data={'content':'another new content'}

        #get method / retrieve
        get_response=self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_status_update(self):
        data=self.create_item()
        data_id=data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id':data_id})
        rud_data={'content':'another new content'}

        #put / update
        put_response=self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response_data=put_response.data
        self.assertEqual(rud_response_data['content'], rud_data['content'])

    def test_status_delete(self):
        data=self.create_item()
        data_id=data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id':data_id})
        rud_data={'content':'another new content'}

        #delete
        del_response=self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        #not found call
        get_response=self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


    def test_status_no_token_create(self):
        #for status object create test
        url = api_reverse('api-status:list')
        data={'content':'some cool test content'}
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Status.objects.count(), 2)


    def test_empty_create_item(self):
        self.status_user_token()

        #for status object create test
        url = api_reverse('api-status:list')
        data={'content':None, 'image':None}
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return response.data


    def test_status_create_with_image(self):
        self.status_user_token()

        #for status object create test
        url = api_reverse('api-status:list')
        #(width, height) = (800,1280)
        image_item = Image.new('RGB', (800, 1280), (0,124,174))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj:
            data={'content':'some cool test content', 'image':None}
            response=self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.count(), 3)
            img_data=response.data.get('image')
            self.assertNotEqual(img_data, None)

        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'testcfeuser')
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)


    def test_status_create_with_image_and_desc(self):
        self.status_user_token()

        #for status object create test
        url = api_reverse('api-status:list')
        #(width, height) = (800,1280)
        image_item = Image.new('RGB', (800, 1280), (0,124,174))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj:
            data={'content':None, 'image':file_obj}
            response=self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.count(), 3)

        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'testcfeuser')
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)

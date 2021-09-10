import uvicorn
import os

if __name__=='__main__':
  os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
  os.environ['CUDA_VISIBLE_DEVICES'] = ''
  uvicorn.run('app.main:app', host='127.0.0.1', port=8080, reload=True)
    
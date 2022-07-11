export default function setPublicPath() {
    return Promise.all([getUrl()]).then(values => {
      const [url] = values
      const webpackPublicPath = url.slice(0, url.lastIndexOf('/') + 1)
  
      __webpack_public_path__ = webpackPublicPath
      return true
    })
  }
  
  function getUrl () {
    return window.System.resolve('@falabella/mf-main')
  }
  
  
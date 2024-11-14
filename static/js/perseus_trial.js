// function slayMedusa() {
//   const url = `/perseus_trial/spawn`;
//   const data = { blessing: blessing };

//   fetch(url, {
//       method: 'POST',
//       headers: {
//           'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(data)
//   })
//       .then(response => {
//           if (response.ok) {
//               return response.blob();
//           } else {
//               throw new Error('Failed to download file');
//           }
//       })
//       .then(blob => {
//           const link = document.createElement('a');
//           link.href = URL.createObjectURL(blob);
//           link.download = 'medusas_head.zip';  
//           link.click();  
//       })
//       .catch(error => {
//           console.error('Error downloading the file:', error);
//       });
// }
// function slayMedusa() {
//   const url = `/perseus_trial/spawn?blessing=${blessing}`;

//   fetch(url)
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
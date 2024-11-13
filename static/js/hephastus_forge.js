// function getTheBox() {
//   const url = `/hephastus_forge/spawn?key=${key}`;

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
//           link.download = 'pandoras_box.zip';  
//           link.click();  
//       })
//       .catch(error => {
//           console.error('Error downloading the file:', error);
//       });
// }
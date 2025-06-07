document.addEventListener('DOMContentLoaded', function() { // dom이... 뭔진 모르겠지만 반드시 있어야 작동을 한다고 함
    const fileInput = document.getElementById('fileInput');
    const button = document.getElementById('uploadButton');

    function isFileSelected() {
        if (fileInput.files.length > 0) {
            button.className = 'enabled';
            button.disabled = false;
        } else {
            button.className = 'disabled';
            button.disabled = true;
        }
    }

    fileInput.addEventListener('change', isFileSelected);

    window.uploadFiles = function() {
        if (fileInput.files.length === 0) {
            alert('경고 : 파일이 선택되지 않았습니다.');
            return;
        }
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        
        fetch('/upload', { // formData를 body에 담아 /upload에 전달
            method: 'POST',
            body: formData
        })
        .then(response => response.json()) // 백엔드 요청 받기
        .then(data => {
            console.log(data);
            if (data.status === 0) {
                alert('성공');
            } else {
                alert('백엔드 오류');
            }
            fileInput.value = '';
            isFileSelected();
        })
        .catch(error => {
            alert(error);
        });
    };

    isFileSelected();
});
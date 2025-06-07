document.addEventListener('DOMContentLoaded', function() { // dom이... 뭔진 모르겠지만 반드시 있어야 작동을 한다고 함
    const fileInput = document.getElementById('fileInput');
    const button = document.getElementById('uploadButton');
    const date = document.getElementById('date');
    const MAX_SIZE = function(){
        const maxSize = fetch('/max-size')
        .then(response => response.json())
        .then(data => {
            return data.max_size;
        })
        .catch(error => {
            console.error('Error:', error);
            return 1;
        });
        return maxSize;
    }
    
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
            alert('오류 : 파일이 선택되지 않았습니다.');
            return;
        }
        if (fileInput.files[0].size > MAX_SIZE) {
            alert('오류 : 파일 크기가 너무 큽니다.');
            return;
        }
        const dateValue = date.value;
        const formData = new FormData();
        console.log(dateValue);
        
        formData.append('file', fileInput.files[0]);
        formData.append('date', dateValue);

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
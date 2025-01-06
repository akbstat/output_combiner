# Combine PDF according configuration

# Configuration
```json
{
    "language": "CN",
    "destination": "D:\\projects\\py\\combiner\\.mock\\destination\\listing.pdf",
    "workspace": "D:\\projects\\py\\combiner\\.mock\\outputs",
    "cover": "",
    "files": [
        {
            "title": "列表 16.2.1.3 受试者治疗完成情况（所有随机化受试者）",
            "path": "D:\\pdf_files\\l-16-2-1-3-ds-trt-rand.pdf"
        },
        {
            "title": "列表 16.2.1.1 受试者筛选失败和随机情况（所有签署知情同意书受试者）",
            "path": "D:\\pdf_files\\l-16-2-1-1-scr-rand-all.pdf"
        },
        {
            "title": "列表 16.2.1.4 受试者试验完成情况（所有随机化受试者）",
            "path": "D:\\pdf_files\\l-16-2-1-4-ds-study-rand.pdf"
        }
    ]
}
```

# Run combine task
```shell
.\combiner.exe D:\projects\py\combiner\.mock\config.json
```
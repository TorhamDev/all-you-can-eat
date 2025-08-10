# 🍽️ All You Can Eat  
**Unlimited file buffet, served hot via FastAPI!**  

---

## 🥢 What is it?  
**All You Can Eat** is a FastAPI-powered API that lets you download any file, with **any name** and **any size** — even *infinite files*.  
Whether you want a **1KB snack** or a **10GB feast**, we’ve got you covered.  

**Example**:  
```
GET host.com/?filename=file.bin&size=10mb
```

---

## 🍔 Features  
- **Name it your way** – Download files with any filename you want.  
- **Choose your portion** – Sizes in `kb`, `mb`, or `gb`.  
- **Infinite mode** – Omit the `size` parameter to get an *endless stream of data*.  
- **Fallback** – Invalid size units default to a **1KB appetizer**.  
- **Ridiculously fast** – Powered by FastAPI for ultra-speed serving.  

---

## 🍟 API Usage  

### Request
```
GET /?filename=<your_filename>&size=<size_with_unit>
```

### Parameters
| Parameter  | Type   | Description                                                  | Default      |
|------------|--------|--------------------------------------------------------------|--------------|
| `filename` | string | Desired file name (e.g., `myvideo.mp4`, `data.bin`)          | Required   |
| `size`     | string | Size with unit: `kb`, `mb`, `gb` (e.g., `10mb`, `1gb`)        | Infinite mode |

---

### Examples

#### 📄 Download a 5MB file named `test.bin`
```
GET /?filename=test.bin&size=5mb
```

#### 📄 Download a 1GB file named `huge.dat`
```
GET /?filename=huge.dat&size=1gb
```

#### ♾️ Infinite file mode  
(*For when you’re really, really hungry…*)  
```
GET /?filename=forever.bin
```
*(Stream until you cancel the download)*


---

## 🧁 License
GNU3 – eat as much as you want 🍽️

---

> ⚠️ **Warning**: Infinite mode will *never stop*. Download responsibly, or your hard drive will feel very full (or very sad) very quickly.

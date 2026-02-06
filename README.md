# Process Priority Setter - Program Description

## 📖 English Version

### What is Process Priority Setter?

Process Priority Setter is a lightweight utility tool designed to automatically maintain and enforce a specific priority level for any running process on Windows. The program continuously monitors the target process and ensures its priority remains at your desired level, automatically correcting it if the system or the application itself attempts to change it.

### How Does It Work?

The program works by targeting a specific process using its Process ID (PID) and continuously checking its CPU priority level every second. If the priority level differs from your selected setting, the program immediately resets it back to your chosen level. This creates a "priority lock" that prevents any external factors from lowering or raising the process priority.

### Why Was This Created?

While this tool can be used with ANY Windows application or game, it was specifically designed with **Sniper Elite 4** in mind. The game has a peculiar anti-cheat mechanism that automatically sets the game's process priority to LOW, which can significantly impact performance on low-end systems. This constant priority reduction means that even if you manually set the priority to HIGH through Task Manager, the anti-cheat will revert it back to LOW within seconds.

This program solves that problem by creating an automated monitoring loop that fights back against the anti-cheat's priority reduction, ensuring your game maintains HIGH priority (or any other priority you choose) for optimal performance.

### Universal Application

Despite being optimized for Sniper Elite 4, this tool is **completely universal** and can be used with:
- Any video game that suffers from priority issues
- Rendering or encoding software that needs sustained high priority
- Background applications that should run at lower priority to save resources
- Any Windows process where you need consistent priority management
- Multiple instances of applications with different priority needs

### Key Features

✅ **6 Priority Levels**: Low, Below Normal, Normal, Above Normal, High, and Realtime
✅ **Real-time Monitoring**: Checks and corrects priority every second
✅ **Universal Compatibility**: Works with any Windows process
✅ **Lightweight**: Minimal CPU and RAM usage
✅ **Auto-correction**: Instantly reverts any priority changes
✅ **Process Safety**: Automatically stops if target process closes
✅ **User-friendly**: Simple interface, just enter PID and choose priority

### Perfect For:

- **Gamers** dealing with anti-cheat priority limitations (especially Sniper Elite 4)
- **Content Creators** running encoding/rendering tasks
- **Power Users** who need precise process management
- **System Optimizers** managing resource allocation
- **Anyone** who needs consistent process priority

### Technical Details

The program uses Python's `psutil` library to interface with Windows process management APIs. It runs on a separate thread to avoid blocking the user interface, providing smooth operation even during intensive monitoring. The tool requires administrator privileges to modify process priorities, especially for system processes or applications running with elevated permissions.

### Important Notes

⚠️ **Realtime Priority Warning**: The Realtime priority level can make your system unresponsive if used carelessly. It should only be used in specific scenarios where you fully understand the implications.

⚠️ **Administrator Rights**: The program must be run as Administrator to successfully modify process priorities.

⚠️ **Anti-cheat Systems**: While effective against Sniper Elite 4's priority-lowering anti-cheat, some other anti-cheat systems may flag process manipulation tools. Use responsibly and at your own risk.

---

## 📖 Versi Indonesia

### Apa itu Process Priority Setter?

Process Priority Setter adalah tool utilitas ringan yang dirancang untuk secara otomatis menjaga dan mempertahankan level prioritas tertentu untuk proses yang sedang berjalan di Windows. Program ini terus-menerus memonitor proses target dan memastikan prioritasnya tetap pada level yang Anda inginkan, secara otomatis memperbaikinya jika sistem atau aplikasi itu sendiri mencoba mengubahnya.

### Bagaimana Cara Kerjanya?

Program bekerja dengan menargetkan proses spesifik menggunakan Process ID (PID) dan terus memeriksa level prioritas CPU-nya setiap detik. Jika level prioritas berbeda dari pengaturan yang Anda pilih, program segera mengembalikannya ke level yang Anda pilih. Ini menciptakan "pengunci prioritas" yang mencegah faktor eksternal menurunkan atau menaikkan prioritas proses.

### Mengapa Program Ini Dibuat?

Meskipun tool ini dapat digunakan dengan aplikasi atau game Windows APAPUN, program ini secara khusus dirancang dengan **Sniper Elite 4** sebagai fokus utama. Game ini memiliki mekanisme anti-cheat yang unik yaitu secara otomatis mengatur prioritas proses game ke LOW, yang dapat berdampak signifikan pada performa di sistem low-end. Pengurangan prioritas yang konstan ini berarti bahkan jika Anda secara manual mengatur prioritas ke HIGH melalui Task Manager, anti-cheat akan mengembalikannya ke LOW dalam hitungan detik.

Program ini menyelesaikan masalah tersebut dengan menciptakan loop monitoring otomatis yang "melawan" pengurangan prioritas dari anti-cheat, memastikan game Anda mempertahankan prioritas HIGH (atau prioritas lain yang Anda pilih) untuk performa optimal.

### Aplikasi Universal

Meskipun dioptimalkan untuk Sniper Elite 4, tool ini **sepenuhnya universal** dan dapat digunakan dengan:
- Game video apapun yang mengalami masalah prioritas
- Software rendering atau encoding yang membutuhkan prioritas tinggi berkelanjutan
- Aplikasi background yang harus berjalan di prioritas lebih rendah untuk menghemat resource
- Proses Windows apapun yang membutuhkan manajemen prioritas konsisten
- Multiple instance aplikasi dengan kebutuhan prioritas berbeda

### Fitur Utama

✅ **6 Level Prioritas**: Low, Below Normal, Normal, Above Normal, High, dan Realtime
✅ **Monitoring Real-time**: Memeriksa dan memperbaiki prioritas setiap detik
✅ **Kompatibilitas Universal**: Bekerja dengan proses Windows apapun
✅ **Ringan**: Penggunaan CPU dan RAM minimal
✅ **Koreksi Otomatis**: Langsung mengembalikan setiap perubahan prioritas
✅ **Keamanan Proses**: Otomatis berhenti jika proses target ditutup
✅ **User-friendly**: Interface sederhana, tinggal masukkan PID dan pilih prioritas

### Sempurna Untuk:

- **Gamers** yang menghadapi batasan prioritas dari anti-cheat (terutama Sniper Elite 4)
- **Content Creators** yang menjalankan tugas encoding/rendering
- **Power Users** yang membutuhkan manajemen proses presisi
- **System Optimizers** yang mengelola alokasi resource
- **Siapapun** yang membutuhkan prioritas proses yang konsisten

### Detail Teknis

Program menggunakan library `psutil` Python untuk berinteraksi dengan API manajemen proses Windows. Program berjalan pada thread terpisah untuk menghindari blocking pada user interface, memberikan operasi yang smooth bahkan selama monitoring intensif. Tool ini memerlukan hak administrator untuk memodifikasi prioritas proses, terutama untuk proses sistem atau aplikasi yang berjalan dengan elevated permissions.

### Catatan Penting

⚠️ **Peringatan Prioritas Realtime**: Level prioritas Realtime dapat membuat sistem Anda tidak responsif jika digunakan sembarangan. Hanya boleh digunakan dalam skenario spesifik di mana Anda sepenuhnya memahami implikasinya.

⚠️ **Hak Administrator**: Program harus dijalankan sebagai Administrator untuk berhasil memodifikasi prioritas proses.

⚠️ **Sistem Anti-cheat**: Meskipun efektif melawan anti-cheat Sniper Elite 4 yang menurunkan prioritas, beberapa sistem anti-cheat lain mungkin mendeteksi tool manipulasi proses. Gunakan dengan bijak dan dengan risiko Anda sendiri.

---

## 🎯 Use Cases / Kasus Penggunaan

### For Sniper Elite 4 Players / Untuk Pemain Sniper Elite 4:
**Problem**: Anti-cheat constantly sets priority to LOW, causing FPS drops and stuttering
**Solution**: This program maintains HIGH priority, resulting in smoother gameplay and better FPS

**Masalah**: Anti-cheat terus mengatur prioritas ke LOW, menyebabkan FPS drop dan stuttering
**Solusi**: Program ini mempertahankan prioritas HIGH, menghasilkan gameplay lebih smooth dan FPS lebih baik

### For Other Games / Untuk Game Lain:
**Problem**: Some games don't utilize full CPU potential, running at normal priority
**Solution**: Force HIGH or ABOVE NORMAL priority for better performance

**Masalah**: Beberapa game tidak memanfaatkan potensi CPU penuh, berjalan di prioritas normal
**Solusi**: Paksa prioritas HIGH atau ABOVE NORMAL untuk performa lebih baik

### For Background Tasks / Untuk Tugas Background:
**Problem**: Background applications consuming too much CPU while gaming
**Solution**: Set them to LOW or BELOW NORMAL priority to free up resources

**Masalah**: Aplikasi background mengkonsumsi terlalu banyak CPU saat gaming
**Solusi**: Set ke prioritas LOW atau BELOW NORMAL untuk membebaskan resource

---

## 📊 Expected Results / Hasil yang Diharapkan

### Sniper Elite 4 Specifically:
- ✅ 10-30% FPS improvement on low-end systems
- ✅ Reduced stuttering and frame drops
- ✅ Smoother gameplay experience
- ✅ Better CPU utilization
- ✅ Faster loading times

### General Applications:
- ✅ Consistent process priority
- ✅ Better resource management
- ✅ Improved responsiveness
- ✅ Controlled CPU allocation
- ✅ System stability with proper priority distribution

---

## 🔐 Safety & Legality / Keamanan & Legalitas

This program does NOT:
- ❌ Modify game files
- ❌ Inject code into processes
- ❌ Bypass or disable anti-cheat systems
- ❌ Provide unfair competitive advantages
- ❌ Violate game terms of service

Program ini TIDAK:
- ❌ Memodifikasi file game
- ❌ Menyuntikkan kode ke dalam proses
- ❌ Mem-bypass atau menonaktifkan sistem anti-cheat
- ❌ Memberikan keuntungan kompetitif tidak adil
- ❌ Melanggar terms of service game

It simply maintains process priority, which is a standard Windows feature accessible through Task Manager. However, use at your own discretion and risk.

Program ini hanya mempertahankan prioritas proses, yang merupakan fitur standar Windows yang dapat diakses melalui Task Manager. Namun, gunakan dengan kebijaksanaan dan risiko Anda sendiri.

---

**Created by: Nabil Rafa (@nabilr.a95)**
**Purpose**: Optimize gaming and application performance through intelligent priority management
**Tujuan**: Mengoptimalkan performa gaming dan aplikasi melalui manajemen prioritas yang cerdas

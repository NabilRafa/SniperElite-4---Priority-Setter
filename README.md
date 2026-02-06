# Process Priority Setter - Program Description

📖 English Version

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

console.log("Fridaa...");

var k32 = Process.getModuleByName("kernel32.dll");
var sleepAddr = k32.findExportByName("Sleep");

if (sleepAddr) {
    console.log("Target Address " + sleepAddr);

    Interceptor.attach(sleepAddr, {
        onEnter: function(args) {
            console.log("Sleep...: " + args[0]);
            args[0] = ptr(0); 
            
            console.log("Bypassed...");
        }
    });
} else {
    console.log("Module ga ditemukan...");
}
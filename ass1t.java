Object deserialize(byte [] stream) {
Constructor aConstructor;
read class_name and class_handle;
if (class_information == null) aConstructor = lookup(class_handle);
else {Class cl = Class.forName(class_name);
read number (n) of instance variables
Class parameterTypes[]= new Class[n];
for (int i=0 to n-1) {
read name and class_name of instance variable i
parameterTypes[i] = Class.forName(class_name);
}
aConstructor = cl.getConstructor(parameterTypes);
map(aConstructor, class_handle);
}

if (next item in stream is object_handle) o = lookup(object_handle);

else {
Object args[] = new Object[n];
for (int i=0 to n-1)
 {
if (next item in stream is primitive) args[i] = read value 
 	else args[i] = deserialize(//rest of stream)}Object o = cnew.newInstance(args);
read object_handle from stream
map(object, object_handle)return 0;
}
}

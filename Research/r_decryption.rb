####DECRYPTION###
print "Enter Cipher Text: "
cipher_text = gets.chomp
cipher_text_ascii = cipher_text.codepoints

print "Enter Secret Key: "
key = gets.chomp
code_key = key.codepoints
minkey = code_key.min
key_length = key.length

#for each ascii code in code_key % minkey
modulus_key = []
code_key.each do |ascii|
    modulus_key.push ascii % minkey
end

#convert the binary representation of the modulus of ascii key
bin_mod_key = []
modulus_key.each do |key|
    bin_mod_key.push key.to_s(2).rjust(key_length, "0")
end

#perform bitwise right shift operation on the bin_mod_key - length of key times !!!SHIFT TRICK
rot_bin_mod_key = []
rot_bin_mod_key[0] = bin_mod_key.last
for i in (0..bin_mod_key.length-2)
    rot_bin_mod_key.push bin_mod_key[i]
end

#convert binary rotated key to decimal
key_after_rot = []
rot_bin_mod_key.each do |key|
    key_after_rot.push key.to_i(2)
end

#add minASCII with key_after_rot
key_after_min_add = []
for i in (0..code_key.length - 1)
    key_after_min_add.push key_after_rot[i] + minkey
end

#key encrypted
final_key = []
key_after_min_add.each do |key|
    final_key.push key
end

#difference of cipher_text_ascii and code_key in another array difference
difference = []
for i in (0..code_key.length-1)
    difference.push cipher_text_ascii[i] - final_key[i]
end

plain_ascii = []
difference.each do |diff|
    plain_ascii.push minkey + diff
end

plain_text = ""
plain_ascii.each do |asc|
    plain_text += asc.chr
end

puts "Plain Text: #{plain_text}"
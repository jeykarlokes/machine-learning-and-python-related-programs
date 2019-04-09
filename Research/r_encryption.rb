puts "Type the Plain Text"
print "> "

plain_text = gets.chomp #get plain plain_text from user

plain_text_ascii = plain_text.codepoints #find the ascii codes for each character in the plain_text

minASCII = plain_text_ascii.min #find the minimum number of the ascii codes

modulus_content = [] #for each ascii % minimum of ascii
plain_text_ascii.each do |ascii|
    modulus_content.push ascii % minASCII
end


puts "Type the Secret Key"
print "> "
encrypt_key = gets.chomp #ask receiver for encryption key

code_key = encrypt_key.codepoints #find the ascii code for the encryption key

minkey = code_key.min #find minimum number of the ascii codes of key

modulus_key = [] #for each ascii code in code_key % minkey
code_key.each do |ascii|
    modulus_key.push ascii % minkey
end

key_length = encrypt_key.length

bin_mod_key = [] #convert the binary representation of the modulus of ascii key
modulus_key.each do |key|
    bin_mod_key.push key.to_s(2).rjust(key_length, "0")
end

rot_bin_mod_key = [] #perform bitwise right shift operation on the bin_mod_key - length of key times !!!SHIFT TRICK
rot_bin_mod_key[0] = bin_mod_key.last
for i in (0..bin_mod_key.length-2)
    rot_bin_mod_key.push bin_mod_key[i]
end

key_after_rot = [] #convert binary rotated key to decimal
rot_bin_mod_key.each do |key|
    key_after_rot.push key.to_i(2)
end

key_after_min_add = [] #add minASCII with key_after_rot
for i in (0..code_key.length - 1)
    key_after_min_add.push key_after_rot[i] + minASCII
end

final_key = [] #key encrypted
key_after_min_add.each do |key|
    final_key.push key.chr
end

cipher_text_ascii = [] #modulus + key after min add for cipher text
for i in (0..modulus_content.length-1)
    cipher_text_ascii.push modulus_content[i] + key_after_min_add[i]
end

cipher_text = "" #cipher text
cipher_text_ascii.each do |key|
    cipher_text += key.chr
end

puts "cipher_text: #{cipher_text}"
# This basic example of the PowerShell to: 
#   create the Organizational Units in the Active Directory,
#   create User's Accouts and add it into OU (Organizational Units).
#
#   CLI application



#
# 1. Import the Module of ActiveDirecoty
#
Import-Module ActiveDirectory

#
# 2. Absolute path of the CSV file - global variable
#
$csv_path = "C:\Lab\lab-18-users.csv"


#
# 3. Function to create OU and user's account
#
function scanFile_createOUUser {
   

    # Check if CSV file exists
    if (Test-Path $csv_path) {

        # Import user from the CSV file:
        $allusers = Import-Csv -Path $csv_path

        # Scan - Iterate through each user
        foreach ($user in $allusers) {

            $firstName  = $user.FirstName
            $lastName   = $user.LastName
            $userName   = $user.UserName
            $Department = $user.Department
            $Password   = $user.Password


            $domainRoot = "DC=greenbloom,DC=local"

      
            $OUPath = "OU=$Department,$domainRoot"
            
            # Check if the department OU exists
            if (-not (Get-ADOrganizationalUnit -Filter {DistinguishedName -eq $OUPath} -ErrorAction SilentlyContinue)) {
                try {
                    # Create the OU if it doesn't exist
                    New-ADOrganizationalUnit -Name $Department -Path $domainRoot
                    Write-Output "Created Organizational Unit: $OUPath"
                }
                catch {
                    Write-Output "Error creating OU: $OUPath. $_"
                }
            } else {
                Write-Output "OU: $Department already exists."
            }


            # Concatenate the full name
            $fullName = "$firstName $lastName"

            # Check if user already exists before creating the user
            $userExist = Get-ADUser -Filter {SamAccountName -eq $userName} -ErrorAction SilentlyContinue
            if ($userExist) {
                Write-Output "User $userName already exists. Skipping creation."
                continue
            }

            try {

                # Create the user in the correct department OU
                New-ADUser -SamAccountName $userName `
                           -UserPrincipalName "$userName@greenbloom.local" `
                           -Name "$firstName $lastName" `
                           -GivenName "$firstName" `
                           -Surname "$lastName" `
                           -Path $OUPath `  # Use dynamic OU for each department
                           -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
                           -Enabled $true `
                           -PasswordNeverExpires $true  # Add this to ensure the password never expires

                #Set-ADUser -Identity $userName -ChangePasswordAtLogon $true
                Set-ADUser -Identity $Username -ChangePasswordAtLogon $true -PasswordNeverExpires $false

                Write-Output "Created user: $fullName ($userName) in $Department"
            }
            catch {
                Write-Output "Error creating user: $fullName. $_"
            }
        }
    }
    else {
        Write-Output " -- The file was not found."
    }
}



#
# 4. Option function
#
function option {
    Write-Host "________________________________"
    Write-Host "0. Exist;"
    Write-Host "1. Add the Users into OU;"
    Write-Host "2. Print all Organization Units;"
    Write-Host "________________________________"

}


#
# 5. Menu function 
#
function menu {

    # Infinite loop 
    while (1) {
       
        option

        # Prompt for user input and attempt to convert it to an integer
        $input = Read-Host " -- Insert a number"
        
        # Regular expression (to valiate the input)
        if ($input -match '^\d+$') {
            $number = [int]$input     #casting
        } else {
            Write-Host "Invalid input, please enter a valid number."
            continue
        }

        
        Write-Host "You entered: $number"
        
        if ( $number -eq 0 ) { 
            Write-Host "I am leaving ..."
            break
        }
        elseif ( $number -eq 1 ) { 
            scanFile_createOUUser
        }

        elseif ( $number -eq 2 ) {
            Write-Host "Printing Organizational Units (OU):"
            $searchBase = "DC=greenbloom,DC=local"
            try {
                Get-ADOrganizationalUnit -Filter * -SearchBase $searchBase | Select-Object Name, DistinguishedName
            } catch {
                Write-Host "Error: Retrieve Organizational Units"
            }
        }
        else {
            Write-Host "Something wrong ..."
        }
    }
}

#
# 6. Main function 
#
function Main {
    menu
}


Main
